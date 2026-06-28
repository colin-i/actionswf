
/*3i flash.display.MovieClip
i flash.display.Shape
i flash.events.Event
i flash.text.TextField
i flash.text.TextFormat
i flash.text.TextFormatAlign
i flash.events.MouseEvent

a MyClip MovieClip*/
	function on_Enter_Frame(){
		if(a){
			_x-=c;
			if(b){
				_y-=c;
				if(_y<=0){
					b=false;
				}
			}else{
				_y+=c;
				if(_y+_height>=Stage.height){
					b=true;
				}
			}
			if(_x<=0){
				a=false;
			}
		}else{
			_x+=c;
			if(b){
				_y-=c;
				if(_y<=0){
					b=false;
				}
			}else{
				_y+=c;
				if(_y+_height>=Stage.height){
					b=true;
				}
			}
			if(_x+_width>=Stage.width){
				a=true;
			}
		}
	}
	// Handlers
	function onClick(){
		trace('Button clicked!');
	}
	function onOver(){
		_alpha= 80;
	}
	function onOut(){
		_alpha= 100;
	}
/*3
	f p*/
		// Simple visual so you can see it
		//3v shape Shape
		beginFill(0x3399FF);//3 l shape
		lineTo(120, 0);lineTo(120, 80);lineTo(0, 80);//3 r shape
		endFill();//3 l shape
		//3d shape

		// a 1/5 margin
		createTextField('label',1,0,16, 120, 48);
		label.text = 'Click';
		label.selectable = false;

		// a 2/3 size format
		var tf = new TextFormat();
		tf.size = 32;
		tf.align = 'center';
		tf.color = 0xff9933;
		label.setTextFormat(tf);

		// Interactivity
		useHandCursor= true;//3 mb
		onRollOver = onOver;//3 o
		onRollOut = onOut;//3 o
		onPress = onClick;//3 o

		//3d label

		onEnterFrame = on_Enter_Frame; //3 o
/*3	}
	n*/
	var c=%u;
	var a=false;var b=false;
//3 }
