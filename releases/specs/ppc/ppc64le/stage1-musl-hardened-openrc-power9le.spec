subarch: power9le
target: stage1
version_stamp: musl-hardened-openrc-@TIMESTAMP@
rel_type: power9le-musl-hardened
profile: default/linux/ppc64le/17.0/musl/hardened
snapshot: @TIMESTAMP@
source_subpath: power9le-musl-hardened/stage3-power9le-musl-hardened-openrc-latest
chost: powerpc64le-gentoo-linux-musl
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world --jobs 8 --load-average 12
portage_confdir: @REPO_DIR@/releases/portage/stages
portage_prefix: releng
repos: /var/db/repos/musl
