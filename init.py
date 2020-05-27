import multiprocessing
from main import roadmap

def worker(workQueue, doneQueue):
	while True:
		job = workQueue.get(True)  # warte auf job
		# job kann z.B. eine Liste oder ein Dictionary sein, je nachdem, was der Hauptprozess reinschreibt
		result = roadmap(job[0], job[1])
		doneQueue.put(result, False)  # schreibe Ergebnis

def work(currentFrameRecord):
	workerCount = 8
	doneQueue = multiprocessing.Queue(workerCount)
	workQueue = multiprocessing.Queue(workerCount)
	instances = []
	for i in range(workerCount):
		instance = multiprocessing.Process(target=worker, args=(workQueue, doneQueue))
		instance.daemon = True
		instance.start()
		instances.append(instance)
	for i in range(workerCount):
		job = [i, currentFrameRecord]
		workQueue.put(job, False)
	result = doneQueue.get(True)  # warte auf erstes Ergebnis
	for instance in instances:
		instance.terminate()
	return result
	# mach was mit result (restliche Worker laufen weiter, werden aber ignoriert)

currentFrameRecord = 4412 #4409
cycle_count = 1
while(True):
	result = work(currentFrameRecord)
	if(result[0] < currentFrameRecord):
		currentFrameRecord = result[0]
	print('cycle {0} done, current record: {1} frames. Record on call {2}.'.format(cycle_count, currentFrameRecord, result[1]))
	raw_input()
	cycle_count += 1