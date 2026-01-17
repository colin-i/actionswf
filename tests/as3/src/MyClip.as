
import flash.display.MovieClip;
import flash.display.Shape;

class MyClip extends MovieClip {
    public function new() {
        super();

        // Simple visual so you can see it
        var shape = new Shape();
        shape.graphics.beginFill(0x3399FF);
        shape.graphics.drawRect(0, 0, 120, 80);
        shape.graphics.endFill();

        addChild(shape);
    }
}
