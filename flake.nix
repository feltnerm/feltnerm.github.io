{
  description = "feltnerm.github.io";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    {
      self,
      nixpkgs,
      treefmt-nix,
    }:

    let
      # The systems supported for this flake
      supportedSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        "aarch64-linux" # 64-bit ARM Linux
        "x86_64-darwin" # 64-bit Intel macOS
        "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper to provide system-specific attributes
      forEachSupportedSystem =
        f:
        nixpkgs.lib.genAttrs supportedSystems (
          system:
          f {
            pkgs = import nixpkgs { inherit system; };
          }
        );

      treefmtEval = forEachSupportedSystem ({ pkgs }: treefmt-nix.lib.evalModule pkgs ./treefmt.nix);

    in
    {
      checks = forEachSupportedSystem (
        { pkgs }:
        {
          formatting = treefmtEval.${pkgs.system}.config.build.check self;
        }
      );

      formatter = forEachSupportedSystem ({ pkgs }: treefmtEval.${pkgs.system}.config.build.wrapper);
      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {
            # The Nix packages provided in the environment
            # Add any you need here
            packages = with pkgs; [ ];

            # Set any environment variables for your dev shell
            env = { };

            # Add any shell logic you want executed any time the environment is activated
            shellHook = '''';
          };
        }
      );
    };
}
