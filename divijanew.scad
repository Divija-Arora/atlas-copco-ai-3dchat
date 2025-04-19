difference() {
    cube([30, 30, 30]);
    translate([15, 15, 25]) cylinder(h = 20, r = 5);
    translate([15, 15, -15]) cylinder(h = 20, r = 5);
    translate([15, -15, 5]) cylinder(h = 20, r = 5);
    translate([-15, 15, 5]) cylinder(h = 20, r = 5);
    translate([-15, -15, 5]) cylinder(h = 20, r = 5);
}