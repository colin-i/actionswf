#!/bin/sh

#1 file.swf  2 what to call (ex: ./a.out ...) or nothing to skip part 2
#is_debug no_clean
#skip_ffdec ffdec
#skip_alternative no_number_check
#scripts

if [ -z "${1}" ]; then echo file path required; exit 1; fi

dname=`dirname ${1}`
if [ -n "${scripts}" ]; then
	scripts=`readlink -f "${scripts}"`
fi
bname=`basename ${1}`

at_start=`pwd`
cd "${dname}" || exit 1

log="${bname}".log.log
if [ ! -e "${log}" ]; then
	log="${bname}".log
	if [ ! -e "${log}" ]; then echo no log; exit 1; fi
fi

folder="${bname%.*}"
if [ -n "${is_debug}" ]; then echo "${folder}"; fi
out="${folder}".dbg

v=
if [ -n "${is_debug}" ]; then v=-v; fi #; set -x

if [ -z "${skip_ffdec}" ]; then
	if [ -z "${ffdec}" ]; then
		ffdec=ffdec
	fi
	if [ -z "${is_debug}" ]; then
		"${ffdec}" -export script "${folder}" "${bname}" > /dev/null || exit 1
	else
		echo ${ffdec} -export script "${folder}" "${bname}"
		"${ffdec}" -export script "${folder}" "${bname}" || exit 1
	fi
fi
mover () {
	if [ -z "${no_clean}" ]; then
		mv ${v} "${@}" || exit 1
	else
		cp ${v} "${@}" || exit 1
	fi
}
if [ -z "${skip_alternative}" ]; then
	mkdir -p "${out}"

	cd "${folder}"

	move () {
		mover "${1}" $2
		if [ -n "${is_debug}" ]; then
			cat ${2}
		fi
	}
	doaction () {
		to=${1}
		shift
		if [ ${#@} = 0 ]; then
			return 0 #is empty
		fi
		for var in "${@}"; do
			f=`echo ${var} | grep -o frame_.*/`   #/ is important to stop the search
			f=$(expr substr ${f} 1 $(echo $(echo -n ${f} | wc -m)-1 | bc))
			#f=${f::-1}
			f=${to}_$(expr substr ${f} 7 $(echo $(echo -n ${f} | wc -m)-6 | bc))
			#f=${to}_${f:6}
			move ${var} ../"${out}"/${f}
		done
		return 1
	}
	number_expected () {
		if [ -z "${no_number_check}" ]; then
			case ${p} in
				''|*[!0-9]*) echo error: Not a number; exit 1 ;;
			esac #This rejects empty strings and strings containing non-digits
		fi
	}
	new_tag () {
		number_expected
		s=${p}
		t= #type
		if [ -n "${is_debug}" ]; then echo id = ${s}; fi
	}

	ainits_ar_key=
	ainits_ar_set () {
		ainits_ar_key="${ainits_ar_key} $1"
	}
	ainits_ar_get () {
		i=0
		for a in ${ainits_ar_key}; do
			if [ $a = $s ]; then
				return 1
			fi
			i=$((i+1))
		done
		return 0 #no ainits
	}
	ainits_counter=1

#	exposprite_ar_key=
#	exposprite_ar_val=
#	exposprite_ar_set () {
#		exposprite_ar_key="${exposprite_ar_key} $1"
#		exposprite_ar_val="${exposprite_ar_val} $2"
#	}
#	exposprite_ar_get () {
#		i=0
#		for a in ${exposprite_ar_key}; do
#			if [ $a = $s ]; then
#				j=0
#				for exposprite_pre in ${exposprite_ar_val}; do
#					if [ $i = $j ]; then
#						return 1
#					fi
#					j=$((j+1))
#				done
#			fi
#			i=$((i+1))
#		done
#		return 0
#	}

	s= #id
	while read p; do
		if [ -z "${s}" ]; then
			new_tag
		else
			if [ -z "${t}" ]; then
				if [ -z "${p}" ]; then
					t=1 #can be show/done/export
				else
					number_expected
					t=2 #action
					at=${p}
					if [ -n "${is_debug}" ]; then echo at = ${at}; fi
					if [ ${at} = 1 ]; then
						ainits_ar_set ${s}
					fi
					#ainits[${s}]=${at}
				fi
			elif [ ${t} = 1 ]; then
				if [ -z "${p}" ]; then
#					t=3
					if [ -n "${is_debug}" ]; then
						echo show
					fi
				else
				#done
					number_expected
					if [ -n "${is_debug}" ]; then echo finalId = ${p}; fi

					doaction ${s} `find -name DoAction.as | grep DefineSprite_"${p}"_`  #exported sprite
					if [ $? = 0 ]; then
						doaction ${s} `find -name DoAction.as | grep DefineSprite_"${p}"/`  #anonymous sprite
						is_ano_sprite=$?
						#else is empty
					else
						is_ano_sprite=0
					fi

					ainits_ar_get; if [ $? = 1 ]; then #button or DoInitAction sprite
						f=scripts/DefineButton2_${p} #anonymous button
						if [ ! -e ${f} ]; then
							f=scripts/DefineButton2_${p}_* #exported button
							if [ ! -e ${f} ]; then f=; fi
						fi
						if [ -n "${f}" ]; then
							f=`echo -n ${f}`/BUTTONCONDACTION' 'on'('release')'.as
						fi
						#f=`find -name BUTTONCONDACTION' 'on'('release')'.as | grep -P DefineButton2_"${p}(/|_)"` #anonymous/exported button with action

						if [ -e "${f}" ]; then #is a button with action
							d=../"${out}"/${s}
							move "${f}" ${d}
							sed -e '1d' -e '$d' -i ${d}  #remove on(release){ ... }
						elif [ ${is_ano_sprite} = 1 ]; then #anonymous sprite init
							if [ ${ainits_counter} != 1 ]; then
								ainits_file=_${ainits_counter}.as
							else
								ainits_file=.as
							fi
							#f=`find -name DoInitAction${ainits_file}`
							move scripts/DoInitAction${ainits_file} ../"${out}"/${s}
							ainits_counter=$((ainits_counter+1))
#						else #exported sprite with action_init
#							exposprite_ar_set $p $s
						fi
					fi
#					s=
				fi
				s=
#			elif [ ${t} = 3 ]; then #show/export
#				if [ -z "${p}" ]; then
#					if [ -n "${is_debug}" ]; then
#						echo show
#					fi
#				else #export
#					if [ -n "${is_debug}" ]; then echo $s is exported as $p; fi
#					exposprite_ar_get $s; if [ $? = 1 ]; then
#						move scripts/$p.as ../"${out}"/${exposprite_pre}
#					fi
#				fi
#				s=
			else
				new_tag
			fi
		fi
	done <../"${log}"

	doaction 0 `find -maxdepth 3 -name DoAction.as`
	cd ..
fi
#part 2
if [ -n "${2}" ]; then
	set -e #at alternative there are return 1 and !=0 grep returns
	mv ${v} "${bname}" "${bname}".orig
	cd "${at_start}"
	${2} || {
		cd "${dname}"
		if [ ! -e "${bname}" ]; then
			mv ${v} "${bname}".orig "${bname}"
		fi
		exit 1
	}
	cd "${dname}"
	diff "${bname}" "${bname}".orig
	if [ -n "${scripts}" ]; then
		mover "${out}"/* "${scripts}"
	fi
	if [ -z "${no_clean}" ]; then
		rm -r ${v} "${out}"  #or rmdir if -n scripts
		rm -r ${v} "${folder}"
		rm "${bname}".orig
	fi
fi
