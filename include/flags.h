
const debug_none=0
const debug_log=0x1
const debug_alt=0x2
const debug_titles=0x4
const debug_x=0x8
const debug_x_pad=0x10

const flag_forin1=0x20
const flag_framesAsShows=0x40
const flag_x=0x80

const flags_x=debug_x|debug_x_pad|flag_x

const flag_pool=0x100     # write if not .pool file else read
const flag_pool_del=0x200 # if write then unlink .pool file
const flags_pool=flag_pool|flag_pool_del
