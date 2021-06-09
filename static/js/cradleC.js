var Engine = Matter.Engine,
  Render = Matter.Render,
  Runner = Matter.Runner,
  Composites = Matter.Composites,
  MouseConstraint = Matter.MouseConstraint,
  Mouse = Matter.Mouse,
  World = Matter.World,
  Constraint = Matter.Constraint,
  Bodies = Matter.Bodies,
  Body = Matter.Body;

// create engine
var engine = Engine.create(), world = engine.world;

// create renderer
var render = Render.create({
  //element: document.body,
  element:document.getElementById('test_2'),
  engine: engine,
  options: {
    width: 800,
    height: 400,
    wireframes: false,
  background: 'rgb(255,255,255)'

  }
});

console.log(Math.floor(Math.random() * 2) + 1  );


Engine.run(engine);

Render.run(render);

var cradleA = Composites.newtonsCradle(200, 15, 7, 30, 220);
Body.translate(cradleA.bodies[0], { x: -100, y: -100 });
Body.translate(cradleA.bodies[1], { x: -100, y: -100 });
Body.translate(cradleA.bodies[2], { x: -100, y: -100 });

/*
for(var c=0;c<cradleA.bodies.length;c++)
{ 
  cradleA.constraints[c].render.strokeStyle = "#000000";
}
*/
for(var c=0;c<cradleA.bodies.length;c++)
{ 
  cradleA.bodies[c].mass == 1;
  cradleA.constraints[c].render.strokeStyle = "#000000";
if ((Math.floor(Math.random() * 2) + 1) == 1) {
  
  cradleA.bodies[c].render.fillStyle =  "#A771B6";
    } else {
  cradleA.bodies[c].render.fillStyle =  "#33D1CC";  }
}


    var mouse = Mouse.create(render.canvas),
        mouseConstraint = MouseConstraint.create(engine, {
            mouse: mouse,
            constraint: {
                stiffness: 0.2,
                render: {
                    visible: false
                }
            }
        });

    World.add(world, mouseConstraint);

    render.mouse = mouse;
           

//engine.world.gravity = {x:0, y:0.8};

World.add(world, [
  cradleA,

]);
