# TODO: consider sound effects, music, colors

> [x] playing Happy Wheels with Segway guy
> happy_wheels.mp4
> [ ] edit in post

Segways are cool, right? But how do they balance?

> [ ] Segway --> segue
> [ ] edit

Well that question's the perfect segue into talking about control theory!

> [x] demo with Kp, Ki, Kd all 0
> demo_zero.mp4
> [ ] edit in post

Left on its own, the Segway, shown here as a cart and pole, will just fall to one side. No matter how close the handle is to being perpendicular to the floor, the acceleration due to gravity compounds the small error until the Segway comes toppling down.

> Manim of 
> random perturbations g*sin(theta)
> ------------------->    gravity   --> e(t)
>         |                              |
>         +------------------------------+
> with the thickness of the arrows changing to indicate the system dynamics
> [x] GravityBlock.mp4
> [ ] edit

We essentially have a positive feedback look for our errors. Random error comes into the system, gravity compounds and amplifies it, 

> same demo except with the sensor below it at the same time
> [x] demo_sensor.mp4
> [ ] edit in post

and our function of angle over time (e) grows increasingly unstable

> close up of the demo with vertical line showing the center of mass
> [x] Closeup.mp4
> [ ] edit

But what about if we change the feedback loop? The source of our error comes from the center of mass of the handle not being directly above the pivot point.

> Manim of the same system except there is a lower loop
> output (wheels go brrr) --> e(t)
>  ^                            |
>  |                            |
>  +- proportional (Kp*e(t)) <--+
> [x] Proportional.mp4
> [ ] edit

> another close up with a transition arrow for the cart to roll to?

Let's use a sensor to measure the error. We'll make the cart roll under the center of mass faster depending on the magnitude of the error.

> demo with Kp > 0, others = 0 with the sensor below it\
> file:///C:/Users/nathanielbd/code/inverted-pendulum/index.html?kp=0.9&ki=0&kd=0
> [x] demo_prop.mp4
> [ ] edit in post

This works pretty well, 

> pull on the handle

except when there's a large disturbance.

> Shade area under the curve on sensor graph
> [x] Auc.mp4
> [ ] edit

Hmm, our proportional feedback worked when the accumulated errors were small, but not when the accumulated errors were large.

> Manim adds Ki \int_0^t e(\tau) d\tau to the feedback loop

To compensate, we can make the cart roll faster proportional to the area under the error curve (the integral). 

> demo with Kp, Ki > 0, other = 0 with the sensor below it

But this doesn't give good results; the compounding factor of gravity causes the system to overshoot. Talk about a wild ride.

> Use Manim to draw tangent line

During the oscillation, the rate of change of the error changes over time. To combat this oscillation, we need to make the cart roll faster proportional to the slope of the error curve (the derivative).

> working demo!

> Manim with the final feedback loop with all 3 PID -- bold them when they are mentioned

So we finally engineered our very own self-balancing system, changing the speed of the cart based on the error, the integral of the error, and the derivative of the error! Control theory and feedback loops form the basis for so many complex systems, from

> some robot

the control of robotics,

> some airplane

the steering of aircraft,

> insulin-glucose loop

and even the amount of sugar in your blood.

> people on Segways "PIDs make Segways go brrr"

So the next time someone tells you they'll never use calculus, that's the perfect segue to mention PIDs and control the situation.

> end screen saying I hand-coded this, thanking the FOSS authors, and linking to the demo
