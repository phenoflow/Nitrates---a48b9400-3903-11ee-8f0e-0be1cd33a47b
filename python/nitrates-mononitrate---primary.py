# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1994","system":"gprdproduct"},{"code":"32841","system":"gprdproduct"},{"code":"33992","system":"gprdproduct"},{"code":"34196","system":"gprdproduct"},{"code":"34426","system":"gprdproduct"},{"code":"34558","system":"gprdproduct"},{"code":"34582","system":"gprdproduct"},{"code":"34951","system":"gprdproduct"},{"code":"41421","system":"gprdproduct"},{"code":"41676","system":"gprdproduct"},{"code":"41687","system":"gprdproduct"},{"code":"41688","system":"gprdproduct"},{"code":"41737","system":"gprdproduct"},{"code":"43421","system":"gprdproduct"},{"code":"46910","system":"gprdproduct"},{"code":"46911","system":"gprdproduct"},{"code":"47803","system":"gprdproduct"},{"code":"47810","system":"gprdproduct"},{"code":"54824","system":"gprdproduct"},{"code":"58133","system":"gprdproduct"},{"code":"58386","system":"gprdproduct"},{"code":"60336","system":"gprdproduct"},{"code":"779","system":"gprdproduct"},{"code":"91","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-mononitrate---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-mononitrate---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-mononitrate---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
