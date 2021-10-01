$(window).ready(function() {
    const canvas = document.querySelector("canvas");

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let c = canvas.getContext("2d");

    //Get orb cords
    let orbCords = []
    let balls = 75;

    for (let i = 0; i<balls; i++) {
        orbCords.push({
            x: Math.random()*innerWidth,
            y: Math.random()*innerHeight,
            radius: Math.floor(Math.random()+Math.random()*4),
            dx: (Math.random()-0.5)*0.2,
            dy: (Math.random()-0.5)*0.2
        });
    }

    function update() {
        for (let i = 0; i<orbCords.length; i++) {
            let orb = orbCords[i];

            if(orb.x < 0 || orb.x > canvas.width){
                orb.dx = -orb.dx;
            }
            if(orb.y < 0 || orb.y > canvas.height){
                orb.dy = -orb.dy;
            }
            orb.x += orb.dx;
            orb.y += orb.dy;
        }

        draw();
    }

    function animate(){
        requestAnimationFrame(animate);
        c.clearRect(0, 0, canvas.width, canvas.height);
        update();
    }

    function draw() {
        //draw lines connecting the orbs
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        c.beginPath();
        for (let i = 0; i<orbCords.length; i++){
            let l1 = orbCords[i] //move to dot
            c.moveTo(l1.x, l1.y);
            for(let j = 0; j < orbCords.length; j++){
                let l2 = orbCords[j];

                if (get_distance(l1, l2)<=150) {
                    c.lineTo(l2.x, l2.y); //create line between pos l1 and pos l2
                }
            }
        }
        c.strokeStyle = "#a986eb";
        c.stroke();

        for (let i = 0; i < orbCords.length; i++){
            let orb = orbCords[i];
            c.beginPath();
            c.arc(orb.x, orb.y, orb.radius, 0, Math.PI*2, false);
            c.stroke();
            c.fillStyle = "#86eba9";
            c.fill();
        }
    }

    function get_distance(origin, new_point){
        let dx = 0; //dist x
        let dy = 0; //dist y

        dx = new_point.x - origin.x;
        dx *= dx;
        dy = new_point.y - origin.y;
        dy *= dy;

        return Math.sqrt(dx + dy);
    }

    animate();
})