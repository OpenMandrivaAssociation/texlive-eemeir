# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eemeir
# catalog-date 2007-02-20 10:49:06 +0100
# catalog-license lppl
# catalog-version 1.1b
Name:		texlive-eemeir
Version:	1.1b
Release:	5
Summary:	Adjust the gender of words in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eemeir
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eemeir.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eemeir.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eemeir.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines macros for third-person singular pronouns (\E, \Em,
\Eir, \Eirs), which expand differently according to a
masculine/feminine switch. (If the switch is 'masculine', they
would expand to 'he', 'him', 'his' and 'his'; if 'feminine',
they would expand to 'she', 'her', 'her' and 'hers". Apart from
the pronouns, one can define 'word pairs', such as
mother/father, daughter/son, and so on. Gender may be defined
once per document, as an environment, or may be flipped on the
fly.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eemeir/eemeir.sty
%doc %{_texmfdistdir}/doc/latex/eemeir/README
%doc %{_texmfdistdir}/doc/latex/eemeir/eemeir.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eemeir/eemeir.dtx
%doc %{_texmfdistdir}/source/latex/eemeir/eemeir.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-2
+ Revision: 751328
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-1
+ Revision: 718310
- texlive-eemeir
- texlive-eemeir
- texlive-eemeir
- texlive-eemeir

