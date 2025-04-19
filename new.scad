
module bracket() {
    difference() {
        cube([100, 20, 40]);
        translate([0, -20, 20]) cube([120, 60, 10]);
    }
}
bracket();