
/*3 import flash.display.MovieClip;
import flash.display.Shape;
import flash.events.Event;

class MyClip extends MovieClip {
	function onEnterFrame(e) {
		if(a){
			x-=c;
			if(b){
				y-=c;
				if(y<=0){
					b=false;
				}
			}else{
				y+=c;
				if(y+height>=stage.stageHeight){
					b=true;
				}
			}
			if(x<=0){
				a=false;
			}
		}else{
			x+=c;
			if(b){
				y-=c;
				if(y<=0){
					b=false;
				}
			}else{
				y+=c;
				if(y+height>=stage.stageHeight){
					b=true;
				}
			}
			if(x+width>=stage.stageWidth){
				a=true;
			}
		}
	}
	public
	function new() {
		super();

		// Simple visual so you can see it
		var shape = new Shape();
		shape.graphics.beginFill(0x3399FF);
		shape.graphics.drawRect(0, 0, 120, 80);
		shape.graphics.endFill();

		addChild(shape);

		addEventListener(Event.ENTER_FRAME, onEnterFrame);
	}
	static
	var c=%u;
	var a=false;var b=false;
}
*/
