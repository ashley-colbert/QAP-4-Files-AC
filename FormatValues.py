def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr



def FDateN(DateValue):
    # will return a value Month, day, year. Ex. June 26, 2023
    
    DateValueStr = DateValue.strftime("%B %d, %Y")

    return DateValueStr

def FDateA(DateValue):
    # Function will accept a value and format it to Month(as a number)-day-yy. ex. Jun-26-23

    DateValueStr = DateValue.strftime("%m-%d-%y")

    return DateValueStr

def FDateT(DateValue):
    # Function will accept a value and format it to Mon day, year - hr:min AM/PM ex. Jun 26, 2023 - 02:15 PM

    DateValueStr = DateValue.strftime("%b %d, %Y - %I:%M %p")

    return DateValueStr

def FDateX(DateValue):
    # Function will accept a value and format it to mon/day/yy. ex. 09/30/23

    DateValueStr = DateValue.strftime("%m/%d/%y")

    return DateValueStr
