import psycopg2
from settings import SPIDER_PSQL_DB

def main():
	num=10
	str="hahahah'%s' '%s'" %(num,num)
	strs="host='%s' dbname='%s' user='%s' password='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['passward'])
	print strs	

if __name__=="__main__":
	main()
