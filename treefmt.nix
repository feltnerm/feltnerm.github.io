# treefmt.nix
{ pkgs, ... }:
{
  # Used to find the project root
  projectRootFile = "flake.nix";
  programs.prettier.enable = true;
  programs.nixfmt.enable = true;
}
