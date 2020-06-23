# TODO: go with
# [ ] protein folding
# [ ] entropy is information/Maxwell's Demon/Reversible Computing
# [x] PID controllers

# TODO: consider (check youtube audio library)
# [ ] sound effects, 
# [ ] music, 
# [ ] colors

# TODO: rerender with production quality

> [x] playing Happy Wheels with Segway guy
> happy_wheels.mp4
> or https://www.pexels.com/video/a-group-of-people-riding-a-two-wheeled-segway-machine-3066434/
> [ ] edit in post

Segways are cool, right? But how do they balance?

> Segway --> segue
> [x] Segue.mp4
> [x] edit

Well that question's the perfect segue into talking about cybernetics!

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
> [x] edit

We essentially have a positive feedback look for our errors. Random error comes into the system, gravity compounds and amplifies it, 

> same demo except with the sensor below it at the same time
> [x] demo_sensor.mp4
> [ ] edit in post

and our function of angle over time (e) grows increasingly unstable

> close up of the demo with vertical line showing the center of mass
> [x] Closeup.mp4
> [x] edit

But what about if we change the feedback loop? The source of our error comes from the center of mass of the handle not being directly above the pivot point. The handle won't fall over if the cart rolls under the center of mass.

> Manim of the same system except there is a lower loop
> output (wheels go brrr) --> e(t)
>  ^                            |
>  |                            |
>  +- proportional (Kp*e(t)) <--+
> [x] Proportional.mp4
> [x] edit

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
> [x] edit (draw data points with Manim instead of screenshot)

Hmm, our proportional feedback worked when the accumulated errors were small, but not when the accumulated errors were large.

> Manim adds Ki \int_0^t e(\tau) d\tau to the feedback loop
> [x] Integral.mp4
> [x] edit so that the P and I have rectangle blocks and have the lines go through them

To compensate, we can make the cart roll faster proportional to the area under the error curve (the integral). 

> demo with Kp, Ki > 0, other = 0 with the sensor below it
> file:///C:/Users/nathanielbd/code/inverted-pendulum/index.html?kp=0.2&ki=0.015&kd=0
> [x] demo_int.mp4
> [ ] edit in post

But this doesn't give good results; momentum causes the system to overshoot. Talk about a wild ride.

> Use Manim to draw tangent line
> [x] Tangent.mp4
> [x] edit (draw data points with Manim instead of screenshot)

During the oscillation, the rate of change of the error changes over time. To combat this oscillation, we need to make the cart roll faster proportional to the slope of the error curve (the derivative).

> working demo!
> file:///C:/Users/nathanielbd/code/inverted-pendulum/index.html?kp=1.6&ki=0.004&kd=26
> [ ] working_demo.mp4
> [ ] edit in post

The system doesn't overshoot and it's stable.

> Manim with the final feedback loop with all 3 PID -- bold them when they are mentioned
> transition so connection to PID acronym is made clear
> [x] PID.mp4

So we finally engineered our very own self-balancing system, changing the speed of the cart based on the error, the integral of the error, and the derivative of the error! A PID controller! Cybernetics and feedback loops form the basis for so many complex systems, from

> some robot
> https://www.pexels.com/video/automatic-chocolate-machine-855117/

the precise control of robotics,

> some airplane
> https://www.pexels.com/video/full-shot-and-close-up-footage-of-a-flying-drone-machine-3764259/

the fine steering of aircraft,

> insulin-glucose loop
> https://upload.wikimedia.org/wikipedia/commons/d/d5/Negative_Feedback_Gif.gif

and even the regulation of the amount of sugar in your blood.

> people on Segways "PIDs make Segways go brrr"
> https://www.pexels.com/video/a-group-of-people-riding-a-two-wheeled-segway-machine-3066434/

In a way, chaos is nature's preferred state, but control theory is our most powerful tool life has and humans have, to maintain more interesting creations.

So the next time someone tells you they'll never use calculus, that's the perfect segue to mention PIDs and control the situation.

> end screen saying I hand-coded this, thanking the FOSS authors, and linking to the demo
> [x] ThankYou.mp4