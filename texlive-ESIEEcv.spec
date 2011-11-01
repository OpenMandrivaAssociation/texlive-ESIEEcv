Name:		texlive-ESIEEcv
Version:	20090430
Release:	1
Summary:	Curriculum vitae for French use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ESIEEcv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ESIEEcv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package allows the user to set up a curriculum vitae as a
French employer will expect.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
