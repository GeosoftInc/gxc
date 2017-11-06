# Geosoft GX for GXC Repository

This is the repository for Geosoft GX Developer support for GX Language development. Refer to the documentation for more information.

[GX Developer documentation](https://geosoftgxdev.atlassian.net/wiki/display/GD/Python+in+GX+Developer)

[Geosoft GX Language](https://geosoftgxdev.atlassian.net/wiki/spaces/GXD93/pages/78020870/Geosoft+GX+Language)

Also see the [Geosoft Inc. organization on Github](https://github.com/GeosoftInc) for the other programming language specific repos.

Quick Start
-----------

### Configuration

Select a __[Release](https://github.com/GeosoftInc/gxc/releases)__ and download the source code compressed file.  Extract to a folder (e.g. ___c:\gxc-9___) on your system. This will contain the following sub-folders:

   | Folder | Content |
   |:------:| ------- |
   | ___examples___ | source code for all Geosoft GXs |
   | ___include___ | GXC header files that document the GX API |

The compiler and support tools are part of your Geosoft Desktop installation. You will need to add the Geosoft Desktop bin directory to your system path so the compiler programs can be found, and set the environment variable __INCLUDE__ to your ___gxc-9\include___ folder.  For example:

```
set PATH="%PATH%;C:\Program Files\Geosoft\Desktop Applications 9\bin"
set include=c:\gxc-9\include
```

#### Compile a GX

A GX will have a _.gxc_ source file and an optional _.grc_ resorce file.  There may also be _.hlp_ files that are used by the resource file.  Compiling is a 2-step process.  For this example navigate to the __gxc-9.3\examples\agggrid__ folder:

```
grc agggrid
gxc agggrid
```

This will create the GX file: __aggrid.gx__.

License
-------
Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)
