//
//  base16.cc
//  License++
//
//  Copyright © 2018-present @abumq (Majid Q.)
//
//  See https://github.com/abumq/licensepp/blob/master/LICENSE
//

#include <Ripe.h>
#include "base16.h"

using namespace licensepp;

std::string Base16::decode(const std::string& encoded)
{
    return Ripe::hexToString(encoded);
}

std::string Base16::encode(const std::string& raw)
{
    return Ripe::stringToHex(raw);
}
