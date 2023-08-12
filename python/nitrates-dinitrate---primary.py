# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1754","system":"gprdproduct"},{"code":"22427","system":"gprdproduct"},{"code":"2933","system":"gprdproduct"},{"code":"34547","system":"gprdproduct"},{"code":"41993","system":"gprdproduct"},{"code":"43524","system":"gprdproduct"},{"code":"4508","system":"gprdproduct"},{"code":"4843","system":"gprdproduct"},{"code":"5004","system":"gprdproduct"},{"code":"6111","system":"gprdproduct"},{"code":"61998","system":"gprdproduct"},{"code":"7760","system":"gprdproduct"},{"code":"8095","system":"gprdproduct"},{"code":"8573","system":"gprdproduct"},{"code":"9497","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-dinitrate---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-dinitrate---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-dinitrate---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
