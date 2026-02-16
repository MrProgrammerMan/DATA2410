{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };
  outputs = inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
      ];

      perSystem = { config, pkgs, ... }: {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python3
          ];
        };
        packages =
        let 
          tex = (pkgs.texlive.withPackages (ps: with ps;[ 
            latexmk
            scheme-small
            ps.import
            minted
          ]));
        in {
          oblig1 = pkgs.stdenv.mkDerivation {
            name = "Obligatory assigment 1 - DATA2410";
            src = ./04-excercises/oblig1;
            buildInputs = [ tex ];
            phases = [ "buildPhase" "installPhase"];
            buildPhase = ''
              cp -r $src/* . #This is hella dumb, but include doesn't work otherwise
              latexmk -pdf -interaction=nonstopmode main.tex
            '';
            installPhase = ''
              mkdir -p $out
              cp main.pdf $out/
            '';
          };
        };
      };
    };
}
