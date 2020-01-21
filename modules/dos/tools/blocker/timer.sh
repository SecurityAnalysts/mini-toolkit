#!/bin/bash


    case "$1" in
        ip)
                sleep 5
                            iptables -I INPUT -s $2 -j DROP
                            iptables -I OUTPUT -s $2 -j DROP
            exit
;;
        *)
            exit
            ;;
    esac
