# CovidPatientQueue_PriorityQueueImplementation

## 1. Problem Statement
At the government hospital treating patients for Covid, the management is preparing a token
system that gives priority to senior citizens who want to get tested over other patients. As the
patients keep coming and registering, they are added to a priority queue from which patient’s
names are called out for testing. Anticipating a rise in the number of cases across the world, an
appointment software has to be developed to manage this priority effectively.
The application should be able to:
a. Take the patient’s age and create a patient ID in the following format: <xxxxyy> where
xxxx is the patient id and
yy is the patient’s age
b. Insert the patient id in the priority queue based on the age of the patient.
c. If x testing counters got vacant, display the next set of patient IDs and corresponding
names that should go for testing and remove them from the priority queue.

## Asks:
1. Implement the above problem statement in Python 3.7 using Heaps.
2. Perform an analysis for the questions above and give the running time in terms of
input size: n.
Data Structures to be used:
PatientRecord: A list containing the patient information including the patient’s name, age and
the patient number (assigned by the program).
TestingQueue: A max heap containing the patient id sorted in order of next patient for testing
based on the age of the patient.

### Patient Record data structure: 

Functions:
1. def registerPatient(self, name, age): This function registers the name and age of the
patient entering the hospital and assigns them an ID that is then used to capture the details
of the patient in the Patient Record. When the program is executed for the first time, the
patient details are loaded from an input file inputPS6a.txt. This is analogous to the list of
patients present at the hospital before the hospital opens.
Input PS6a format:
Surya, 60
Ajay, 54
Rishi, 57
After all records are read from the inputPS6a file, and the queue is sorted, the queue should
be output to the file outputPS6.txt in the below format.

---- registerPatient ---------------
No of patients added: 3
Refreshed queue:
100160, Surya
100357, Rishi
100254, Ajay
----------------------------------------------
Thereafter, new patients will be input through another file inputPS6b.txt and identified with
the tag newPatient.
newPatient: John, 55
After every new patient in the input PS6b is inserted into the patient record the heap will
have to be refreshed and the new queue should be output to the file outputPS6.txt in the
below format.

---- new patient entered---------------
Patient details: John, 55, 100455
Refreshed queue:
100260, Surya
100357, Rishi
100455, John
100554, Ajay
----------------------------------------------

2. def enqueuePatient(self, PatId): This function assigns the patient a place in the max heap
depending on their age. The patient id is inserted into the max heap. This function should
be called every time a new patient is added and should run a sort after adding the patient id
to keep the testing queue updated as per the age condition.
3. def nextPatient(self): This function prints the next x number of patient_IDs and their names
that are next in line for testing. This function is called when the program encounters a next
patient tag from the inputPS6b.txt file. The format of the next patient will be

nextPatient: 1
The function will read the x number of patient details that should be output. The output is
pushed to the file outputPS6.txt in the below format.
---- next patient : 1 ---------------
Next patient for testing is: 100260, Surya
----------------------------------------------
4. def _dequeuePatient(self, PatId): This function removes from the queue the patient ID that
has completed the testing and updates the queue. The function is called from the nextPatient
function itself after the next patients name is displayed.
5. Include all other functions required to support the operations of these basic functions.

## 2. Sample file formats
Sample Input file
The inputPS6a.txt file contains the first set of registrations.
Sample inputPS6a.txt
Surya, 60
Ajay, 54
Rishi, 57
Sample inputPS6b.txt
newPatient: John, 55
nextPatient: 1
newPatient: Pradeep, 45
nextPatient: 2
nextPatient: 1
newPatient: Sandeep, 60
nextPatient: 3
Sample outputPS6.txt
---- initial queue ---------------
No of patients added: 3
Refreshed queue:
100160, Surya
100357, Rishi
100254, Ajay
-----------------------------------------
----------------------------------------------
---- new patient entered---------------
Patient details: John, 55, 100455
Refreshed queue:
100260, Surya
100357, Rishi
100455, John
100554, Ajay
----------------------------------------------
---- next patient: 1 ---------------
Next patient for testing is: 100260, Surya
----------------------------------------------
----------------------------------------------

## 3. Deliverables
a. A1_PS6_DC_[Group id] package folder containing modules and package files for the
entire program code and associated functions
b. inputPS6a.txt file used for testing
c. inputPS6b.txt file used for testing
d. outputPS6.txt file containing the output of the program
e. analysisPS6.txt file containing the running time analysis for the program.
