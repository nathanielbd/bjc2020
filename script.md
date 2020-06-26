# BRUNIOR JAKETHROUGH CHALLENGE

> https://www.pexels.com/video/a-group-of-people-riding-a-two-wheeled-segway-machine-3066434/

Segways are cool, right? But how do they balance?

> Segue.mp4

Well that question's the perfect segue into talking about cybernetics! Cybernetics is the study of how complex systems maintain themselves.

> demo with Kp, Ki, Kd all 0

For example, the Segway, shown here as a cart and pole, will just fall to one side when left on its own. No matter how close the handle is to being perpendicular to the floor, the acceleration due to gravity compounds the small error until the Segway comes toppling down.

> GravityBlock.mp4

We essentially have a positive feedback look for our errors. Random error comes into the system, gravity compounds and amplifies it, 

> same demo except with the sensor below it at the same time

and our function of error over time grows increasingly unstable

> Closeup.mp4

But what about if we change the feedback loop? The source of our error comes from the center of mass of the handle not being directly above the pivot point. The handle won't fall over if the cart rolls under the center of mass before it falls down.

> Proportional.mp4

Let's use a sensor to measure the error. We'll make the cart roll under the center of mass faster depending on the magnitude of the error.

> demo with Kp > 0, others = 0 with the sensor below it

This works pretty well, 

> pull on the handle

except when there's a large disturbance.

> Auc.mp4

Hmm, our proportional feedback worked when the accumulated errors were small, but not when the accumulated errors were large.

> Integral.mp4

To compensate, we can make the cart roll faster proportional to the area under the error curve (the integral). 

> demo with Kp, Ki > 0, other = 0 with the sensor below it

But this doesn't give good results either; momentum causes the system to overshoot. Talk about a wild ride.

> Tangent.mp4

We want to bring the error to zero, but our cart rolls too quickly and passes by the center of mass. On the graph, this shows up as a steep line while crossing the horizontal axis. We want the slope of the line to be flat so when the error reaches zero, it stays zero. To do this, we can make the cart slow down proportional to the slope of the error curve (the derivative).

> working demo!

The system doesn't overshoot and it's stable. We flattened the curve!

> PID.mp4

So we finally engineered our very own self-balancing system, based on the error, the integral of the error, and the derivative of the error! Cybernetics and feedback loops, like this PID controller, form the basis for so many complex systems, from

> https://www.pexels.com/video/automatic-chocolate-machine-855117/

the precise control of robotics,

> https://www.pexels.com/video/full-shot-and-close-up-footage-of-a-flying-drone-machine-3764259/

the fine steering of aircraft,

> https://upload.wikimedia.org/wikipedia/commons/d/d5/Negative_Feedback_Gif.gif

and even the regulation of the amount of sugar in your blood.

> boids.js with a setTimeout to change from chaotic to coherent

In a way, chaos is nature's preferred state, but cybernetics is the most powerful tool we have to maintain more interesting creations.

> Segway man again, to end with the start in a poetic manner

So the next time someone tells you you'll never use calculus, that's the perfect segue to mention PIDs and control the situation.

> ThankYou.mp4
