%global tl_name bbold
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Sans serif blackboard bold
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bbold
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A geometric sans serif blackboard bold font, for use in mathematics;
Metafont sources are provided, as well as macros for use with LaTeX. The
Sauter font package has Metafont parameter source files for building the
fonts at more sizes than you could reasonably imagine. See the
blackboard sampler for a feel for the font's appearance.

