difference() {
    union() {
        cube([20, 20, 10]);
        translate([5, 5, 0])
            cylinder(h = 10, r = 2.5, center = true);
        translate([-5, -5, 0])
            cylinder(h = 10, r = 2.5, center = true);
    }
    translate([0, 0, 10])
        cylinder(h = 5, r = 2.5, center = true);
}