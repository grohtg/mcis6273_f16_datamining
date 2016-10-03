import csv

def prepocess_separate_by_state(state='AR'):
    state = state.lower()

    with open('14zpallagi.csv', 'r') as fi, \
         open('2014_{}_agi_data.csv'.format(state), 'wb') as fo:
        reader = csv.DictReader(fi)
        writer = csv.DictWriter(fo, fieldnames=reader.fieldnames)
        writer.writeheader()

        for l in reader:
            if l['STATE'].lower().strip() == state:
                writer.writerow(l)

if __name__ == "__main__":
    prepocess_separate_by_state('AR')
