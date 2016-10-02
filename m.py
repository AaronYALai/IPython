from mrjob.job import MRJob
import time

class count(MRJob):
    def mapper(self,key,line):
    	for word in line.strip().split():
            yield word,1

    def combiner(self,key,occur):
        yield key,sum(occur)

    def reducer(self,key,occurence):
        yield key,sum(occurence)


if __name__ == '__main__':
    start = time.clock()
    count.run()
    end = time.clock()
    print end-start