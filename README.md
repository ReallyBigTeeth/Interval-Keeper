# Interval-Keeper
A simple application to keep track of intervals while training indoors on a treadmill or cycle trainer.

This is a work in progress.  I am currently learning the QT framework, so for now this application just runs in a console. Currently this application will only run in Windows as it uses the winsound library for audio tones.

Upon running the application you will be asked to input the details of your first set of intervals or segment.  The questions are pretty straight forward:

**1** - Give your first segment a simple description.  This is just a reminder for you of details of the upcoming segment or intervals.

**2** - How many intervals will you be doing for this segment?  Enter an integer of 1 or greater.  Enter 1 if you just want to time something like a single tempo session.

**3** - How long are is the on time?  This will be for how long your doing your hard work. Input time in HH:MM:SS.  For intervals of 45 seconds, you could enter 0:0:45 or 00:00:45, or 000:0:45.  For an hour twenty minute segment, you could enter 1:20:00, or 01:20:0,  just make sure you include integers for all three fields.

**4** - How much rest between intervals?  Enter this data the same as your "on" time: HH:MM:SS.

One you have finished entering the details of your first set of intervals or segment, you will be prompted to enter the details for a second segment or set of intervals.  You can create as many sets as you like.  If you are ready to start your workout, hit <ENTER> throught the next set of questions until you are prompted with the description of your first interval set.  Hit <ENTER> again and your fist interval will begin after a 5 second count down.  Four tones will sound just before the begining of each rest or on segment and series of tones to let you know when the current segment or set of intervals is complete.  The program will then pause and display the description of the next segment or set of intervals.  Hit enter to continue.

ReallyBigTeeth
