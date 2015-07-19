# revision 17187
# category Package
# catalog-ctan /fonts/bbold
# catalog-date 2010-02-15 23:28:51 +0100
# catalog-license bsd
# catalog-version 1.01
Name:		texlive-bbold
Version:	1.01
Release:	10
Summary:	Sans serif blackboard bold
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bbold
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbold.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A geometric sans serif blackboard bold font, for use in
mathematics; MetaFont sources are provided, as well as macros
for use with LaTeX. The Sauter font package has MetaFont
parameter source files for building the fonts at more sizes
than you could reasonably imagine. See the blackboard sampler
for a feel for the font's appearance.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bbold/bbbase.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbgreekl.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbgreeku.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbligs.mf
%{_texmfdistdir}/fonts/source/public/bbold/bblower.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbnum.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold10.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold12.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold17.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold5.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold6.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold7.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold8.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbold9.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbparams.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbpunc.mf
%{_texmfdistdir}/fonts/source/public/bbold/bbupper.mf
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold10.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold12.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold17.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold5.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold6.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold7.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold8.tfm
%{_texmfdistdir}/fonts/tfm/public/bbold/bbold9.tfm
%{_texmfdistdir}/tex/latex/bbold/Ubbold.fd
%{_texmfdistdir}/tex/latex/bbold/bbold.sty
%doc %{_texmfdistdir}/doc/latex/bbold/INSTALL
%doc %{_texmfdistdir}/doc/latex/bbold/README
%doc %{_texmfdistdir}/doc/latex/bbold/bbold.pdf
#- source
%doc %{_texmfdistdir}/source/latex/bbold/bbold.dtx
%doc %{_texmfdistdir}/source/latex/bbold/bbold.ins
%doc %{_texmfdistdir}/source/latex/bbold/fonttabl.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 749508
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 717891
- texlive-bbold
- texlive-bbold
- texlive-bbold
- texlive-bbold
- texlive-bbold

