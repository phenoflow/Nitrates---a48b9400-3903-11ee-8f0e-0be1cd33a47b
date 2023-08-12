# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"10607","system":"gprdproduct"},{"code":"11978","system":"gprdproduct"},{"code":"12968","system":"gprdproduct"},{"code":"13090","system":"gprdproduct"},{"code":"17867","system":"gprdproduct"},{"code":"24651","system":"gprdproduct"},{"code":"28803","system":"gprdproduct"},{"code":"29777","system":"gprdproduct"},{"code":"32442","system":"gprdproduct"},{"code":"3645","system":"gprdproduct"},{"code":"41014","system":"gprdproduct"},{"code":"521","system":"gprdproduct"},{"code":"60055","system":"gprdproduct"},{"code":"7327","system":"gprdproduct"},{"code":"7767","system":"gprdproduct"},{"code":"8539","system":"gprdproduct"},{"code":"8790","system":"gprdproduct"},{"code":"8902","system":"gprdproduct"},{"code":"9335","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-125mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-125mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-125mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
