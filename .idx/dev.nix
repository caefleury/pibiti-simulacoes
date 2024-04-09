{ pkgs, ... }: {

  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311Packages.pytest
  ];

  # Sets environment variables in the workspace
  env = {
    SOME_ENV_VAR = "PYTHONPATH=$PWD/src/utils";
  };

  # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"

  # Enable previews and customize configuration
}