# Rust
if [ -d $HOME/.cargo ]; then
  source $HOME/.cargo/env
  export RUST_SRC_PATH="$(rustc --print sysroot)/lib/rustlib/src/rust/src"
fi
