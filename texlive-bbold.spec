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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A geometric sans serif blackboard bold font, for use in mathematics;
Metafont sources are provided, as well as macros for use with LaTeX. The
Sauter font package has Metafont parameter source files for building the
fonts at more sizes than you could reasonably imagine. See the
blackboard sampler for a feel for the font's appearance.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bbold
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/source/latex/bbold
%dir %{_datadir}/texmf-dist/tex/latex/bbold
%dir %{_datadir}/texmf-dist/fonts/source/public/bbold
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bbold
%doc %{_datadir}/texmf-dist/doc/latex/bbold/INSTALL
%doc %{_datadir}/texmf-dist/doc/latex/bbold/README
%doc %{_datadir}/texmf-dist/doc/latex/bbold/bbold.pdf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbgreekl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbgreeku.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbligs.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bblower.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbnum.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold12.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold17.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbold9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbparams.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbpunc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bbold/bbupper.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold12.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold17.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bbold/bbold9.tfm
%doc %{_datadir}/texmf-dist/source/latex/bbold/bbold.dtx
%doc %{_datadir}/texmf-dist/source/latex/bbold/bbold.ins
%doc %{_datadir}/texmf-dist/source/latex/bbold/fonttabl.sty
%{_datadir}/texmf-dist/tex/latex/bbold/Ubbold.fd
%{_datadir}/texmf-dist/tex/latex/bbold/bbold.sty
