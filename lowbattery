#!/bin/sh

export DISPLAY=:0
export XDG_RUNTIME_DIR=/run/user/$(id -u)

acpi -b | awk -F'[,:%]' '{print $2, $3}' | {
	read -r status capacity

	if [ "$status" = Discharging -a "$capacity" -lt 20 ]; then
		/bin/notify-send -u critical "LOW BATTERY";
        /bin/mpv ~/Coding/scripts/hangouts.mp3 --volume=60
	fi
}

exit 0
