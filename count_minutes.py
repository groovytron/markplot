import sys
import re
from itertools import tee

def create_dict(filename):
    with open(filename) as f:
        time_regex = re.compile(r"\| \d+$")
        activity_regex = re.compile(r"^(?:Documentation|Test|Développement|Environnement de développement|Environnement de test|Étude de faisabilité)")
        row_time = None
        doc_dic = dict()

        for i in range(2):
            f.readline()
        for line in f:
            row_time = time_regex.findall(line)
            row_activity = activity_regex.findall(line)
            if row_time != None and len(row_activity):
                row_activity = row_activity[0]
                row_time = int(row_time[0][2:])
                if doc_dic.get(row_activity, None) != None:
                    doc_dic[row_activity] += row_time
                else:
                    doc_dic[row_activity] = row_time
                #print(row_activity, ":", row_time)
            else:
                raise NameError('Missing time or activity in the following line: ', line)
        return doc_dic;

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("falsy call")
    else:
        activity_histo = create_dict(sys.argv[1])
        print(activity_histo)
        total_minutes = sum(activity_histo.values())
        minutes = total_minutes % 60
        hours = int(total_minutes / 60)
        print("Time passed:", hours, "hours and", minutes, "minutes")
