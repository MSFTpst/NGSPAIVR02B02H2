from dtaf_core.lib.tklib.infra.bios.bios import BIOS_KNOB_BMC


numa_cluster_disabled_bmc = (BIOS_KNOB_BMC(name='AcPwrRcvry'), 'Last')
numa_cluster_enabled_bmc = (BIOS_KNOB_BMC(name='AcPwrRcvry'), 'On')

hyper_thread_enabled_bmc = (BIOS_KNOB_BMC(name="MultiThreaded"), "Enabled")
hyper_thread_disabled_bmc = (BIOS_KNOB_BMC(name="MultiThreaded"), "Disabled")

disable_SpeedStep_xmlcli = (BIOS_KNOB_BMC(name='SubNumaCluster'), 'Disabled')
