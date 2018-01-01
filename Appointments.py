from unitType import encode, decode, Unit
def encodeAppointments(appointments):
    #express appointments as intervals over time line
    for i, appointment in enumerate(appointments):
        appointments[i] = [encode(appointment[0]),encode(appointment[1])]
    appointments.sort(key=lambda x:x[1])
    appointmentIntervals = []
    alreadyProccessed = []
    for i, appointment in enumerate(appointments):
        startBlock, endBlock = appointment[0], appointment[1]
        if alreadyProccessed.__contains__([startBlock,endBlock]):
            continue#prevent duplication
        for otherStart, otherStop in appointments[i + 1:]:
            if otherStart <= endBlock and otherStart >= startBlock:
                # overlap occured
                alreadyProccessed.append([otherStart,otherStop])
                if endBlock < otherStop:
                    #overlap not equal -> extend block
                    endBlock = otherStop
        appointmentIntervals.append([startBlock, endBlock])
    return appointmentIntervals
def encodeAvailability(appointments, fromThisTime, tillThisTime):
    #express availability as intervals over time line
    if type(appointments[0][0]) is str:
        raise Exception("pass encoded appointments")
    availability = []
    last = fromThisTime
    for start, end in appointments:
        #available from end of last appointment till begining of next appointment
        availability.append([last,start])
        last = end
    availability.append([last,tillThisTime])
    return availability
def encodeOpenings(availability):
    #appointment openings are
    appointmentOpenings = []
    for start, stop in availability:
        #how many half hours segments are in open interval
        segmentCount = Unit(stop) - Unit(start)
        for offset in range(int(segmentCount)):
            appointmentOpenings.append([start+offset,start+offset+1])
    return appointmentOpenings
def decodeOpenings(openings):
    for i, opening in enumerate(openings):
        openings[i] = (decode(opening[0]),decode(opening[1]))
