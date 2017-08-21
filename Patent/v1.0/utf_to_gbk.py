import os,sys,re,csv
reload(sys)
sys.setdefaultencoding('gbk')

def write(r):
    outfile = open('test.csv', 'ab')
    writer = csv.writer(outfile)
    writer.writerow(r)
    outfile.close()
    return 0


if __name__ == '__main__':

    with open('CN-BIBS-ABSS-10-A_20170725.csv') as f:
        # cv = f.readlines()
        cv = csv.reader(f)
        for line in cv:
            write(line)
        f.close()
    print 'done'

