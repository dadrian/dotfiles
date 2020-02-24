# Guess common install locations if not provided
if [ -z ${GOOGLE_CLOUD_SDK_INSTALL+x} ]; then
  if [ $(uname -s) = "Darwin" ]; then
    # Brew Cask or Home Directory
    BREW_PREFIX=$(brew --prefix)
    BREW_CASK_CLOUD_INSTALL="${BREW_PREFIX}/Caskroom/google-cloud-sdk/latest/google-cloud-sdk"
    HOME_DIR_CLOUD_INSTALL="${HOME}/google-cloud-sdk"

    if [ -d "${BREW_CASK_CLOUD_INSTALL}" ]; then
      GOOGLE_CLOUD_SDK_INSTALL="${BREW_CASK_CLOUD_INSTALL}"
    elif [ -d "${HOME_DIR_CLOUD_INSTALL}" ]; then
      GOOGLE_CLOUD_SDK_INSTALL="${HOME_DIR_CLOUD_INSTALL}"
    fi
  fi
fi

# If we found an install location, source the completion files.
if [ ! -z ${GOOGLE_CLOUD_SDK_INSTALL+x} ]; then
  # The next line updates PATH for the Google Cloud SDK.
  source "${GOOGLE_CLOUD_SDK_INSTALL}/path.${DADRIAN_SHELL_NAME}.inc"

  # The next line enables shell command completion for gcloud.
  source "${GOOGLE_CLOUD_SDK_INSTALL}/completion.${DADRIAN_SHELL_NAME}.inc"
fi
