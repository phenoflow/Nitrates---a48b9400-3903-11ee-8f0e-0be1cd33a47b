# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"10147","system":"gprdproduct"},{"code":"11596","system":"gprdproduct"},{"code":"13530","system":"gprdproduct"},{"code":"20322","system":"gprdproduct"},{"code":"22358","system":"gprdproduct"},{"code":"23011","system":"gprdproduct"},{"code":"24683","system":"gprdproduct"},{"code":"25276","system":"gprdproduct"},{"code":"31475","system":"gprdproduct"},{"code":"32059","system":"gprdproduct"},{"code":"32253","system":"gprdproduct"},{"code":"39130","system":"gprdproduct"},{"code":"39135","system":"gprdproduct"},{"code":"43615","system":"gprdproduct"},{"code":"44712","system":"gprdproduct"},{"code":"60941","system":"gprdproduct"},{"code":"7746","system":"gprdproduct"},{"code":"8940","system":"gprdproduct"},{"code":"9719","system":"gprdproduct"},{"code":"9908","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-tablet---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-tablet---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-tablet---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
