
const no_pointer=0  #NULL

const ActionIf=0x9D                #1

const ActionSetVariable=0x1D       #2
const ActionDelete=0x3A            #2
const ActionDelete2=0x3B           #2
const ActionDefineLocal=0x3C       #2
const ActionDefineLocal2=0x41      #2
const ActionSetMember=0x4F         #2

const block_end=0xfbBBbbBB            #1 F
const block_else_end=0xfcCCccCC       #1
const args_end=0xfeEEeeEE             #C
const math_end=0xffFFffFF             #0 RI RG

const call_action_left=0xf1011010     #1
const call_action_right=0xf2022020    #RG
const function_action=0xf3033030      #1
const new_action=0xf4044040           #RI
const square_bracket_start=0xf5055050 #M
const compare_action=0xf7077070       #OC
const parenthesis_start=0xf8088080    #RG
const ifElse_start=0xfe0EE0e0         #RI
const member_end=0xff0FF0f0           #M

const else_flag=0x40<<24              #1

const ap_double=6              #RG
const ap_Integer=7             #RG
const ap_Constant8=8           #RG
const ActionSubtract=0x0B      #O
const ActionMultiply=0x0C      #O
const ActionDivide=0x0D        #O
const ActionNot=0x12           #OC
const ActionGetVariable=0x1C   #RG
const ActionModulo=0x3F        #O
const ActionAdd2=0x47          #O
const ActionLess2=0x48         #OC
const ActionEquals2=0x49       #OC
const ActionGetMember=0x4E     #RG
const ActionBitAnd=0x60        #O
const ActionBitOr=0x61         #O
const ActionBitXor=0x62        #O
const ActionBitLShift=0x63     #O
const ActionBitRShift=0x64     #O
const ActionBitURShift=0x65    #O
const ActionGreater=0x67       #OC

const ActionEndFlag=0           #at builtin case only to test(not to write)
const ActionNextFrame=0x04      #builtin
const ActionPreviousFrame=0x05  #builtin
const ActionPlay=0x06           #builtin
const ActionStop=0x07           #builtin
const ActionToInteger=0x18      #builtin
const ActionTrace=0x26          #builtin
const ActionRandomNumber=0x30   #builtin
const ActionCharToAscii=0x32    #builtin
const ActionAsciiToChar=0x33    #builtin
const ActionCallFunction=0x3D
const ActionNewObject=0x40
const ActionTypeOf=0x44         #builtin
const ActionCallMethod=0x52
const ActionNewMethod=0x53
const ActionGotoFrame=0x81      #builtin
const ActionStoreRegister=0x87
const ActionConstantPool=0x88
const ActionPush=0x96
    const ap_Null=2
    const ap_Undefined=3
    const ap_RegisterNumber=4
    const ap_Boolean=5
    const ap_Constant16=9
const ActionJump=0x99
const ActionDefineFunction=0x9B


#const ActionAdd=0x0A
const ActionAnd=0x10
const ActionOr=0x11
const ActionPop=0x17
const ActionReturn=0x3E
const ActionEnumerate=0x46
const ActionPushDuplicate=0x4C
const ActionIncrement=0x50
const ActionDecrement=0x51
#const ActionGotoFrame2=0x9F

const mixt_equal=0xf6066060
const break_flag=0xf9099090
const continue_flag=0xfa0AA0a0
#
const for_marker=0xfb0BB0b0
const for_three=0xfc0CC0c0
const inter_for=0xfd0DD0d0

const brace_blocks_function=0x7fFFffFF

const consecutive_flag=0x80<<24
#const all_flags=consecutive_flag|else_flag
const normal_marker=0x01010202
const if_marker=0x03030404
const while_marker=0x05050606
const function_marker=0x07070808

const whileblock_end=0xfdDDddDD
