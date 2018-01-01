def encode(time):
    #example does not provide am pm.
    #am pm implicit possible due to no overlap of pm am work day hours
    hours, minutes = time.split(":")
    halfHours, minutes = 2*int(hours), int(minutes)
    halfHours += minutes // 30
    minutes -= (minutes//30) * 30
    #convert to military time
    if int(hours) < 8:#if pm as inferred by context
        halfHours += 2*12
    #reduce demensions of unit
        #possible because time forms a line with minutes and smaller frames of time expressed in decimal range
    halfHours += 100**-1 * minutes
    return halfHours
def decode(time):
    #timeInTermsOfAppointments -> stringTime
    minutes = str(int((time%2//1)*30 + round(100*(time%(time//1)))))
    hours = str(int(time//2 - 12*(time//24)))
    if hours == "0":
        hours = "12"
    while len(minutes) < 2:
        minutes += "0"
    return hours+":"+minutes
class Unit:
    # continuous scaler with hybrid numeral system
        # decimal is base 30, none decimal is base 24
    # unit is timeInTermsOfAppointments
    # origin is 12 am
    def __init__(self, time):
        if type(time) is str:
            self.halfHours = encode(time)
        elif type(time) is float:
            self.halfHours = time
        else:
            raise Exception("Enexpected Logic")
    def __sub__(self, other):
        #example 15.20 - 13.25 = 1.25 one halfHour, 25 min difference
        halfHours, minutes = divmod(self.halfHours,1)
        otherHalf, otherMin = divmod(other.halfHours,1)
        resultHalf = halfHours - otherHalf
        resultMin = minutes - otherMin
        if resultMin < 0:
            resultHalf -= 1
            resultMin += .30
        return resultHalf + resultMin
