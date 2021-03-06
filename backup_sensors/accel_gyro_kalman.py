
'''RateAxz = InvertAxz * (AdcGyroXZ * Vref / 1023 - VzeroRate) / Sensitivity , where InvertAxz is 1 or -1

same test cane be done for RateAyz , by rotating the device around the X axis, and you can identify which gyroscope output corresponds to RateAyz, and if it needs to be inverted. Once you have the value for InvertAyz, you should use the following formula to calculate RateAyz:

RateAyz = InvertAyz * (AdcGyroYZ * Vref / 1023 - VzeroRate) / Sensitivity

If you would do these tests on Acc_Gyro board you would get following results:

- the output pin for RateAxz is GX4 and InvertAxz = -1.
- the output pin for RateAyz is GY4 and InvertAyz = -1'''

'''In the next steps I will introduce an algorithm that was inspired by some ideas used in Kalman filter, however it is by far more simple and easier to implement on embedded devices. Before that let's see first what we want our algorithm to calculate. Well , it is the direction of gravitation force vector R = [Rx,Ry,Rz] from which we can derive other values like Axr,Ayr,Azr or cosX,cosY,cosZ that will give us an idea about the inclination of our device relative to the ground plane, we discuss the relation between these values in Part 1. One might say - don't we already have these values Rx, Ry , Rz from Eq.2 in Part 1 ? Well yes, but remember that these values are derived from accelerometer data only, so if you would be to use them directly in your application you might get more noise than your application can tolerate. To avoid further confusion let's re-define the accelerometer measurements as follows:'''

from bstem.platform import AdCord
from math import *
import time

ad=AdCord()
#Racc - is the inertial force vector as measured by accelerometer, that consists of following components (projections on X,Y,Z axes):

Racc=[]
Rxacc=[]
Ryacc=[]
Rzacc=[]
Racc.append(ad.accelerometer.value)
Rxacc.append(Racc[0][0])
Ryacc.append(Racc[0][1])
Rzacc.append(Racc[0][2]) #not used value
'''RxAcc = (AdcRx * Vref / 1023 - VzeroG) / Sensitivity
RyAcc = (AdcRy * Vref / 1023 - VzeroG) / Sensitivity
RzAcc = (AdcRz * Vref / 1023 - VzeroG) / Sensitivity'''

'''So far we have a set of measured values that we can obtain purely from accelerometer ADC values. We'll call this set of data a "vector" and we'll use the following notation.

Racc = [RxAcc,RyAcc,RzAcc]

Because these components of Racc can be obtained from accelerometer data , we can consider it an input to our algorithm.

Please note that because Racc measures the gravitation force you'll be correct if you assume that the length of this vector defined as follows is equal or close to 1g.'''

magRacc=sqrt(pow(Rxacc[0],2)+pow(Ryacc[0],2))

#|Racc| = SQRT(RxAcc^2 +RyAcc^2 + RzAcc^2),

'''However to be sure it makes sense to update this vector as follows:

Racc(normalized) = [RxAcc/|Racc| , RyAcc/|Racc| , RzAcc/|Racc|].

This will ensure the length of your normalized Racc vector is always 1.'''
lst=list(Racc[0])
lst[0]=Rxacc[0]/magRacc
lst[1]=Ryacc[0]/magRacc
Racc[0]=tuple(lst)


#Next we'll introduce a new vector and we'll call it

#Rest = [RxEst,RyEst,RzEst]
Rest=[]
Rxest=[]
Ryest=[]
#Rzest=[]
'''This will be the output of our algorithm , these are corrected values based on gyroscope data and based on past estimated data.

Here is what our algorithm will do:
- accelerometer tells us: "You are now at position Racc"
- we say "Thank you, but let me check",
- then correct this information with gyroscope data as well as with past Rest data and we output a new estimated vector Rest. 
- we consider Rest to be our "best bet" as to the current position of the device.

Let's see how we can make it work.'''

#1. We'll start our sequence by trusting our accelerometer and assigning:
Rest.append(Racc[0])
Rxest.append(Rest[0][0])
Ryest.append(Rest[0][1])
#Rzest=Rest[0][2] #not used value
#By the way remember Rest and Racc are vectors , so the above equation is just a simple way to write 3 sets of equations, and avoid repetition:

'''RxEst(0) = RxAcc(0)
RyEst(0) = RyAcc(0)
RzEst(0) = RzAcc(0)'''

'''Next we'll do regular measurements at equal time intervals of T seconds, and we'll obtain new measurements that we'll define as Racc(1), Racc(2) , Racc(3) and so on. We'll also issue new estimates at each time intervals Rest(1), Rest(2), Rest(3) and so on.'''

n=0
Axy=[]
RateAxy=[]
RateAxy.append(ad.gyroscope.z)
Axy.append({Rxest[0],Ryest[0]})
f=open("reading.txt",'w')
while(True):
	time.sleep(0.01)
	if(ad.accelerometer.x==0 and ad.accelerometer.y==0):
		continue
	n+=1
	Racc.append(ad.accelerometer.value)
	Rxacc.append(Racc[n][0])
	Ryacc.append(Racc[n][1])
	magRacc=sqrt(pow(Rxacc[n],2)+pow(Ryacc[n],2))
	
	lst=list(Racc[n])
	lst[0]=Rxacc[0]/magRacc
	lst[1]=Ryacc[0]/magRacc
	Racc[n]=tuple(lst)

	
	#gyroscope
	#Rgyro=ad.gyroscope.value
	RateAxy.append(ad.gyroscope.z)
	Axy.append((atan2(Rxest[n-1],Ryest[n-1]))+RateAxy[n]*(.01)) #Axy[n]
	RateAxyAvg=((RateAxy[n]+RateAxy[n-1])/2)
	Axy[n]=((atan2(Rxest[n-1],Ryest[n-1]))+RateAxyAvg*(.01))

	Rxgyro=sin(Axy[n])
	Rygyro=cos(Axy[n])

	wGyro=5 #5-20
	Rxest.append((Rxacc[n] + Rxgyro * wGyro ) / (1 + wGyro))
	Ryest.append((Ryacc[n] + Rygyro * wGyro ) / (1 + wGyro))
	magRest=sqrt(pow(Rxest[n],2)+pow(Ryest[n],2))
	Rxest[n]=Rxest[n]/magRest
	Ryest[n]=Ryest[n]/magRest
	#finally
	#print("x:",Rxest[n]," y:",Ryest[n])
	print('.')
	
	f.write("x:")
	f.write(str(Rxest[n]))
	f.write("     ,y:")
	f.write(str(Ryest[n]))
	f.write('\n')

f.close()
'''Suppose we're at step n. We have two known sets of values that we'd like to use:

Rest(n-1) - our previous estimate, with Rest(0) = Racc(0)
Racc(n) - our current accelerometer measurement

Before we can calculate Rest(n) , let's introduce a new measured value, that we can obtain from our gyroscope and a previous estimate.

We'll call it Rgyro , and it is also a vector consisting of 3 components:

Rgyro = [RxGyro,RyGyro,RzGyro]

We'll calculate this vector one component at a time. We'll start with RxGyro.'''
		
'''Let's start by observing the following relation in our gyroscope model, from the right-angle triangle formed by Rz and Rxz we can derive that:

tan(Axz) = Rx/Rz => Axz = atan2(Rx,Rz)

Atan2 might be a function you never used before, it is similar to atan, except it returns values in range of (-PI,PI) as opposed to (-PI/2,PI/2) as returned by atan, and it takes 2 arguments instead of one. It allows us to convert the two values of Rx,Rz to angles in the full range of 360 degrees (-PI to PI). You can read more about atan2 here.'''
#------------------------------------------------------------------------------------------------------------------------------
	
'''
So knowing RxEst(n-1) , and RzEst(n-1) we can find:

Axz(n-1) = atan2( RxEst(n-1) , RzEst(n-1) ).

Remember that gyroscope measures the rate of change of the Axz angle. So we can estimate the new angle Axz(n) as follows:

Axz(n) = Axz(n-1) + RateAxz(n) * T

Remember that RateAxz can be obtained from our gyroscope ADC readings. A more precise formula can use an average rotation rate calculated as follows:

RateAxzAvg = ( RateAxz(n) + RateAxz(n-1) ) / 2 
Axz(n) = Axz(n-1) + RateAxzAvg * T

The same way we can find:

Ayz(n) = Ayz(n-1) + RateAyz(n) * T
'''
	

'''---------------------------------------------------------------------------------------------------------------------------------------------

Ok so now we have Axz(n) and Ayz(n). Where do we go from here to deduct RxGyro/RyGyro ? From Eq. 1 we can write the length of vector Rgyro as follows:

|Rgyro| = SQRT(RxGyro^2 + RyGyro^2 + RzGyro^2)

Also because we normalized our Racc vector, we may assume that it's length is 1 and it hasn't changed after the rotation, so it is relatively safe to write:

|Rgyro| = 1

Let's adopt a temporary shorter notation for the calculations below:

x =RxGyro , y=RyGyro, z=RzGyro

Using the relations above we can write:

x = x / 1 = x / SQRT(x^2+y^2+z^2)

Let's divide numerator and denominator of fraction by SQRT(x^2 + z^2)

x = ( x / SQRT(x^2 + z^2) ) / SQRT( (x^2 + y^2 + z^2) / (x^2 + z^2) )

Note that x / SQRT(x^2 + z^2) = sin(Axz), so:

x = sin(Axz) / SQRT (1 + y^2 / (x^2 + z^2) )

Now multiply numerator and denominator of fraction inside SQRT by z^2

x = sin(Axz) / SQRT (1 + y^2  * z ^2 / (z^2 * (x^2 + z^2)) )

Note that z / SQRT(x^2 + z^2) = cos(Axz) and y / z = tan(Ayz), so finally:

x = sin(Axz) / SQRT (1 + cos(Axz)^2 * tan(Ayz)^2 )

Going back to our notation we get:

RxGyro = sin(Axz(n)) / SQRT (1 + cos(Axz(n))^2 * tan(Ayz(n))^2 )

same way we find that

RyGyro = sin(Ayz(n)) / SQRT (1 + cos(Ayz(n))^2 * tan(Axz(n))^2 )

Now, finally we can find:

RzGyro  =  Sign(RzGyro)*SQRT(1 - RxGyro^2 - RyGyro^2).

Where Sign(RzGyro) = 1 when RzGyro>=0 , and Sign(RzGyro) = -1 when RzGyro<0.

One simple way to estimate this is to take:

Sign(RzGyro) = Sign(RzEst(n-1))

In practice be careful when RzEst(n-1) is close to 0. You may skip the gyro phase altogether in this case and assign:  Rgyro = Rest(n-1). Rz is used as a reference for calculating Axz and Ayz angles and when it's close to 0, values may oveflow and trigger bad results. You'll be in domain of large floating point numbers where tan() / atan() function implementations may lack precision.

So let's recap what we have so far, we are at step n of our algorithm and we have calculated the following values:

Racc - current readings from our accelerometer
Rgyro - obtained from Rest(n-1) and current gyroscope readings

Which values do we use to calculate the updated estimate Rest(n) ? You probably guessed that we'll use both. We'll use a weighted average, so that:

Rest(n) = (Racc * w1 + Rgyro * w2 ) / (w1 + w2)

We can simplify this formula by dividing both numerator and denominator of the fraction by w1.

Rest(n) = (Racc * w1/w1 + Rgyro * w2/w1 ) / (w1/w1 + w2/w1)

and after substituting w2/w1 = wGyro we get:

Rest(n) = (Racc + Rgyro * wGyro ) / (1 + wGyro)

In the above forumula wGyro tells us how much we trust our gyro compared to our accelerometer. This value can be chosen experimentally usually values between 5..20 will trigger good results.

The main difference of this algorithm from Kalman filter is that this weight is relatively fixed , whereas in Kalman filter the weights are permanently updated based on the measured noise of the accelerometer readings. Kalman filter is focused at giving you "the best" theoretical results, whereas this algorithm can give you results "good enough" for your practical application. You can implement an algorithm that adjusts wGyro depending on some noise factors that you measure, but fixed values will work well for most applications.

We are one step away from getting our updated estimated values:

RxEst(n) = (RxAcc + RxGyro * wGyro ) / (1 + wGyro)
RyEst(n) = (RyAcc + RyGyro * wGyro ) / (1 + wGyro)
RzEst(n) = (RzAcc + RzGyro * wGyro ) / (1 + wGyro)

Now let's  normalize this vector again:

R = SQRT(RxEst(n) ^2 + RyEst(n)^2 +  RzEst(n)^2 )

RxEst(n) = RxEst(n)/R
RyEst(n) = RyEst(n)/R
RzEst(n) = RzEst(n)/R

And we're ready to repeat our loop again.

---------------------------------------------------------------------------------------------------------------------------------------------'''
