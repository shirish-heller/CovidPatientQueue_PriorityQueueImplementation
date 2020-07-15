class PatientRecord:
	def __init__(self, name, age, Pid):
		self.name = name
		self.age = int(str(age).strip(" "))
		self.PatId = str(Pid) + str(age).strip(" ")
		self.left = None
		self.right = None

class TestingQueue:
	def __init__(self, registerPatientsFilePath, newPatientsFilePath, outputFilePath):
		self.heap=[]
		self.registerPatientsFilePath=registerPatientsFilePath
		self.newPatientsFilePath=newPatientsFilePath
		self.outputFilePath=outputFilePath
		self.patientCount=0
		self.initializePatientList()

	def get_parent_index(self, i):
		return ((i+1)//2)-1

	def get_left_child_index(self, i):
		return 2*(i+1)-1

	def get_right_child_index(self, i):
		return 2*(i+1)+1-1

	def has_left_child(self, i):
		return self.get_left_child_index(i) < len(self.heap)

	def has_right_child(self, i):
		return self.get_right_child_index(i) < len(self.heap)

	def has_parent(self, i):
		return self.get_parent_index(i)>=0

	def print_heap(self):
		print("/n")
		print(self.heap)

	def enqueuePatient(self, patient):
		self.heap.append(patient)
		self.__heapifyBottomToTop__()
	
	def writeAfterPatientsDequed(self, patientsDequed):
		try:
			out_file=open(self.outputFilePath, 'a+')
			out_file.write("----next patient : "+str(len(patientsDequed)) +"---------------\n")
			for patient in patientsDequed:
				out_file.write("Next patient for testing is: "+str(patient.PatId)+ ", " + str(patient.name) +"\n")
			out_file.write("----------------------------------------------\n")
		except Exception as e:
			print("Error writing writeAfterPatientsDequed details in outputPS6 file")

	def dequePatients(self, patientsToDeque):
		patientsDequed=[]
		while patientsToDeque>0:
			if(len(self.heap)>0):
				patientsDequed.append(self.heap[0])
				self.__swapHeapNodes__(0,-1)
				print("deleting " + str(self.heap[-1].age))
				del self.heap[-1]
				self.__heapifyTopToBottom__()
				patientsToDeque=patientsToDeque-1
			else:
				break
		self.writeAfterPatientsDequed(patientsDequed)

	def writeAfterRegisterPatients(self):
		try:		
			out_file=open(self.outputFilePath, 'w')
			out_file.write("----registerPatient---------------\n")
			out_file.write("No of patients added: " + str(len(self.heap)) + "\n")
			out_file.write("\nRefreshed queue: \n")
			for patient in self.heap:
				out_file.write(str(patient.PatId) + ", " + str(patient.name) +"\n")
			out_file.write("----------------------------------------------\n")
			out_file.write("\n")
			print("----------------------------------------------\n")
		except Exception as e:
			print("Error writing registerPatient details in outputPS6 file")

	def __swapHeapNodes__(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __heapifyTopToBottom__(self):
		i=0
		has_left_child=self.has_left_child(i)
		while(has_left_child):
			has_right_child=self.has_right_child(i)
			currentNode = self.heap[i]
			leftChild = self.heap[self.get_left_child_index(i)]
			if(has_left_child and has_right_child):
				rightChild = self.heap[self.get_right_child_index(i)]
				if(currentNode.age>leftChild.age and currentNode.age>rightChild.age):
					# this means that heap is in correct order already (max-heap)
					break
				else:
					# index_bigger_node=self.heap.index(max(leftChild.age, rightChild.age))
					index_bigger_node= self.heap.index(leftChild) if leftChild.age>rightChild.age else self.heap.index(rightChild)
					self.__swapHeapNodes__(i, index_bigger_node)
					i=index_bigger_node
					has_left_child=self.has_left_child(i)

			else:
				if(leftChild.age>currentNode.age):
					leftIndex=self.heap.index(leftChild)
					self.__swapHeapNodes__(i, leftIndex)
					i=leftIndex
					has_left_child=self.has_left_child(i)

				else:
					# this means that heap is in correct order already (max-heap)
					break

	def __heapifyBottomToTop__(self):
		i=len(self.heap)-1
		while(self.has_parent(i)):
			parentNodeIndex=self.get_parent_index(i)
			if(self.heap[parentNodeIndex].age < self.heap[i].age):
				self.__swapHeapNodes__(i, parentNodeIndex)
			else:
				break
			i=parentNodeIndex

	def initializePatientList(self):
		try:		
			f = open(self.registerPatientsFilePath, 'r')
			data = f.readlines()
			for entry in data:
				patientData = entry.split(",")
				print(patientData[0], " \n")
				print(patientData[1], " \n")
				pid = self.patientCount+1000
				patient = PatientRecord(patientData[0].strip("\n"), patientData[1].strip("\n"), pid)
				self.enqueuePatient(patient)
				self.patientCount=self.patientCount+1
				self.writeAfterRegisterPatients()

		except Exception as e:
			print("Error in reading PatientRecords file", e)

	def writeNewPatientDetails(self, newPatient):
		try:
			f=open(self.outputFilePath, 'a+')
			f.write("----new patient entered---------------\n")
			f.write("Patient details: " + str(newPatient.name)+", "+str(newPatient.age)+", "+newPatient.PatId+"\n\n")
			f.write("Refreshed queue: \n")
			for patient in self.heap:
				f.write(str(patient.PatId) + ", " + str(patient.name) +"\n")
			f.write("----------------------------------------------\n")
		except Exception as e:
			print("Error writing new patient details in outputPS6 file")

	def updatePatients(self):
		try:
			f=open(self.newPatientsFilePath, 'r')
			data=f.readlines()
			for line in data:
				if(len(self.heap)>0):
					if(line.find("newPatient")!=-1):
						patientData=line.split(":")[1].split(",")
						pid = self.patientCount+1000
						newPatient= PatientRecord(patientData[0].strip(" "), patientData[1].strip("\n"), pid)
						self.enqueuePatient(newPatient)
						self.patientCount=self.patientCount+1
						self.writeNewPatientDetails(newPatient)
					elif(line.find("nextPatient")!=-1):
						if(len(self.heap)==0):
							break
						nextPatientCount=line.split(":")[1].strip(" ").strip("\n")
						self.dequePatients(int(nextPatientCount))

					else:
						print("Every line must contain nextPatient or newPatient.")
				else:
					break

		except Exception as e:
			print("Error in reading newPatients record file", e)