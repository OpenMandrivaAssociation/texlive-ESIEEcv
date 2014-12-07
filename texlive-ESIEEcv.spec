# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ESIEEcv
# catalog-date 2009-04-30 00:32:08 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ESIEEcv
Version:	20090430
Release:	9
Summary:	Curriculum vitae for French use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ESIEEcv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to set up a curriculum vitae as a
French employer will expect.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ESIEEcv/ESIEEcv.sty
%doc %{_texmfdistdir}/doc/latex/ESIEEcv/ESIEEcv.pdf
%doc %{_texmfdistdir}/doc/latex/ESIEEcv/cvtest.pdf
%doc %{_texmfdistdir}/doc/latex/ESIEEcv/cvtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/ESIEEcv/ESIEEcv.dtx
%doc %{_texmfdistdir}/source/latex/ESIEEcv/ESIEEcv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090430-2
+ Revision: 751574
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090430-1
+ Revision: 718363
- texlive-ESIEEcv
- texlive-ESIEEcv
- texlive-ESIEEcv
- texlive-ESIEEcv
- texlive-ESIEEcv
- texlive-ESIEEcv

