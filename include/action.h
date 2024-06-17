
const no_pointer=0  #NULL

const ActionReturn=0x3E            #1
const ActionIf=0x9D                #1

const ActionDelete=0x3A            #2
const ActionDelete2=0x3B           #2
const ActionDefineLocal2=0x41      #2

const ActionSetVariable=0x1D       #L
const ActionDefineLocal=0x3C       #L
const ActionSetMember=0x4F         #L

const math_end=0xffFFffFF             #0 RG RH
const args_end=0xfeEEeeEE             #C
const whileblock_end=0xfdDDddDD       #1 FR
const block_else_end=0xfcCCccCC       #1
const block_end=0xfbBBbbBB            #F IF
const member_end=0xfaAAaaAA           #M

const call_action_left=0xf1011010     #1
const call_action_right=0xf2022020    #RH
const function_action=0xf3033030      #1
const new_action=0xf4044040           #RG
const square_bracket_start=0xf5055050 #M
const mixt_equal=0xf6066060           #R
const compare_action=0xf7077070       #OC
const parenthesis_start=0xf8088080    #RH
const break_flag=0xf9099090           #1
const continue_flag=0xfa0AA0a0        #1
const for_three=0xfb0BB0b0            #FR
const inter_for=0xfc0CC0c0            #FR
const ifElse_start=0xfd0DD0d0         #RG
const for=0xfe0EE0e0                  #1

const no_flag=0                        #code only
const top_flag=0x10<<24                #code only
const skip_flag=0x20<<24               #code only
const else_flag=0x40<<24               #1
const consecutive_flag=0x80<<24        #parse only
const brace_blocks_function=0x7fFFffFF #code only

const normal_marker=0x01010202        #parse only
const if_marker=0x03030404            #parse only
const while_marker=0x05050606         #1
const function_marker=0x07070808      #parse only
const forin_marker=0x09090a0a         #code only

const ActionSubtract=0x0B      #OP
const ActionMultiply=0x0C      #OP
const ActionDivide=0x0D        #OP
const ActionAnd=0x10           #O
const ActionOr=0x11            #O
const ActionNot=0x12           #OC
const ActionGetVariable=0x1C   #RT
const ActionModulo=0x3F        #OP
const ActionAdd2=0x47          #OP
const ActionLess2=0x48         #OC
const ActionEquals2=0x49       #OC
const ActionGetMember=0x4E     #RT
const ActionIncrement=0x50     #R
const ActionDecrement=0x51     #R
const ActionBitAnd=0x60        #OP
const ActionBitOr=0x61         #OP
const ActionBitXor=0x62        #OP
const ActionBitLShift=0x63     #OP
const ActionBitRShift=0x64     #OP
const ActionBitURShift=0x65    #OP
const ActionGreater=0x67       #OC
const ActionPush=0x96
	const ap_Null=2
	const ap_Undefined=3
	const ap_RegisterNumber=4
	const ap_Boolean=5
	const ap_double=6        #RH
	const ap_Integer=7       #RH
	const ap_Constant8=8     #RH
	const ap_Constant16=9

const ActionEndFlag=0           #at builtin case only to test(not to write)
const ActionNextFrame=0x04      #builtin
const ActionPreviousFrame=0x05  #builtin
const ActionPlay=0x06           #builtin
const ActionStop=0x07           #builtin
#const ActionAdd=0x0A
const ActionPop=0x17
const ActionToInteger=0x18      #builtin
const ActionTrace=0x26          #builtin
const ActionRandomNumber=0x30   #builtin
const ActionCharToAscii=0x32    #builtin
const ActionAsciiToChar=0x33    #builtin
const ActionCallFunction=0x3D
const ActionNewObject=0x40
const ActionTypeOf=0x44         #builtin
const ActionEnumerate=0x46
const ActionPushDuplicate=0x4C
const ActionStackSwap=0x4D
const ActionCallMethod=0x52
const ActionNewMethod=0x53
const ActionEnumerate2=0x55
const ActionGotoFrame=0x81      #builtin
const ActionStoreRegister=0x87
const ActionConstantPool=0x88
const ActionJump=0x99
const ActionDefineFunction=0x9B
#const ActionGotoFrame2=0x9F
