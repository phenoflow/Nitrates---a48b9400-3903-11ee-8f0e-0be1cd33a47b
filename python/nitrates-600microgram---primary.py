# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"1145","system":"gprdproduct"},{"code":"1184","system":"gprdproduct"},{"code":"1260","system":"gprdproduct"},{"code":"1539","system":"gprdproduct"},{"code":"15746","system":"gprdproduct"},{"code":"1685","system":"gprdproduct"},{"code":"1793","system":"gprdproduct"},{"code":"20915","system":"gprdproduct"},{"code":"2144","system":"gprdproduct"},{"code":"2145","system":"gprdproduct"},{"code":"28030","system":"gprdproduct"},{"code":"2991","system":"gprdproduct"},{"code":"31247","system":"gprdproduct"},{"code":"33991","system":"gprdproduct"},{"code":"37242","system":"gprdproduct"},{"code":"3909","system":"gprdproduct"},{"code":"39265","system":"gprdproduct"},{"code":"40388","system":"gprdproduct"},{"code":"42214","system":"gprdproduct"},{"code":"4529","system":"gprdproduct"},{"code":"4626","system":"gprdproduct"},{"code":"4677","system":"gprdproduct"},{"code":"47805","system":"gprdproduct"},{"code":"4785","system":"gprdproduct"},{"code":"48232","system":"gprdproduct"},{"code":"4887","system":"gprdproduct"},{"code":"50809","system":"gprdproduct"},{"code":"53134","system":"gprdproduct"},{"code":"53416","system":"gprdproduct"},{"code":"55089","system":"gprdproduct"},{"code":"55520","system":"gprdproduct"},{"code":"56011","system":"gprdproduct"},{"code":"56446","system":"gprdproduct"},{"code":"57963","system":"gprdproduct"},{"code":"62154","system":"gprdproduct"},{"code":"6239","system":"gprdproduct"},{"code":"7317","system":"gprdproduct"},{"code":"7795","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-600microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-600microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-600microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
