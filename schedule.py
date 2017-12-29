from unitType import encode
from Appointments import encodeAppointements, encodeAvailability, encodeOpenings, decodeOpenings
def team_availability(appointments):
    lunch = ["12:00","1:00"]
    appointments.append(lunch)
    #express appointments as intervals over time line
    appointments = encodeAppointements(appointments)
    startOfDay, endOfDay = encode("8:30"), encode("5:00")
    #express availability as intervals over time segment
    availability = encodeAvailability(appointments, startOfDay, endOfDay)
    # chop availablity into 30 minute openings
    openings = encodeOpenings(availability)
    #Decode openings to string time
    decodeOpenings(openings)
    return openings
appointments = [['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30']]
print(team_availability(appointments))

# Unit test decode must == encode for range encode(start stop work day)
#team_availability([['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30']])
#[['8:30', '9:00'], ['11:30', '12:00'], ['1:00', '1:30'], ['1:30', '2:00'], ['2:00', '2:30'], ['3:30', '4:00'], ['4:00', '4:30'], ['4:30', '5:00']]
#8:30-5:00, with lunch from 12:00-1:00, we have 8 engineers on our team with appointments at 9:00-9:30, 9:00-11:30, 10:00-11:00, 2:30-3:00, 2:30-3:30

