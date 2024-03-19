({ inputs, ... }:

  {
    perSystem = { self', config, system, pkgs, lib, ... }:
      let
        mkNixpkgs = nixpkgs:
          import nixpkgs {
            inherit system;
            overlays = [ inputs.nix-extra.overlays.default ];
            config = { allowUnfree = true; };
          };

      in {
        _module.args.pkgs = mkNixpkgs inputs.nixpkgs;
        devShells = {
          default = pkgs.mkShell {
            buildInputs = [

              (pkgs.python3.withPackages (p:
                lib.attrValues { inherit (p) fractopo jupyterlab ipython; }))

            ];
            shellHook = config.pre-commit.installationScript + ''
              export PROJECT_DIR="$PWD"
            '';
          };

        };

        checks = {
          test = let
            script = pkgs.writeShellApplication {
              name = "test";
              runtimeInputs = self'.devShells.default.buildInputs;
              text = let
                notebooks = [ "network.ipynb" "network_no_topology.ipynb" ];
                mkCmds = baseCmd:
                  builtins.concatStringsSep "\n"
                  (builtins.map baseCmd notebooks);
                conversionCmds = mkCmds (notebook:
                  "jupyter nbconvert --clear-output --execute ${notebook} --inplace");

              in ''
                ${conversionCmds}
                fractopo tracevalidate --help
                fractopo network --help
              '';

            };
          in pkgs.runCommand "test" { } ''
            mkdir $out
            cd $out
            cp -r -L --no-preserve all ${./data} ./data
            cp -r -L --no-preserve all ${./network.ipynb} ./network.ipynb
            cp -r -L --no-preserve all ${
              ./network_no_topology.ipynb
            } ./network_no_topology.ipynb
            ${script}/bin/test
          '';
        };

        pre-commit = {
          check.enable = true;
          settings.hooks = {
            nixfmt.enable = true;
            black.enable = true;
            black-nb.enable = true;
            nbstripout.enable = true;
            isort = { enable = true; };
            shellcheck.enable = true;
            statix.enable = true;
            deadnix.enable = true;
            rstcheck.enable = true;
            yamllint = { enable = true; };
            commitizen.enable = true;
            ruff = { enable = true; };
          };

        };
      };

  })
